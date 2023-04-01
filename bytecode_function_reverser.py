from pyevmasm import disassemble_hex
import re
import requests
from colorama import Fore

dis_ass = disassemble_hex('608060405234801561001057600080fd5b50610150806100206000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c80632e64cec11461003b5780636057361d14610059575b600080fd5b610043610075565b60405161005091906100a1565b60405180910390f35b610073600480360381019061006e91906100ed565b61007e565b005b60008054905090565b8060008190555050565b6000819050919050565b61009b81610088565b82525050565b60006020820190506100b66000830184610092565b92915050565b600080fd5b6100ca81610088565b81146100d557600080fd5b50565b6000813590506100e7816100c1565b92915050565b600060208284031215610103576101026100bc565b5b6000610111848285016100d8565b9150509291505056fea2646970667358221220322c78243e61b783558509c9cc22cb8493dde6925aa5e89a08cdf6e22f279ef164736f6c63430008120033').split('\n')

signatures = [line.strip() for line in open('signatures.txt')]

signature_from_asm = []

# disassemble bytecode to asm
# parse out all the functions signatures
# match signatures to local database of signatures
# lookup the functions online .. or local

print(type(dis_ass))

# checks the disassembled out put if certain opcode, func. signatures are within it
for instruction in dis_ass:
    # checks if it is of 16 length, and doesn't have duplicate
    if len(instruction) == 16 and (instruction[-8:] not in signature_from_asm):
        signature_from_asm.append(instruction[-8:])
print(signature_from_asm)
print(len(signature_from_asm))

# check if the function signature gotten matches whats on function signature database
for signature in signature_from_asm:
    if signature in signatures:
        r = requests.get(
            f'https://api.etherface.io/v1/signatures/hash/all/{signature}/1', verify=False)  # verify=False is used to ignore SSL certificate errors

        # find all matches of "text":", and remove the rest of the string, leaving only the function name
        matches = re.findall(r'(?<="text":")(.*?)(?=",)', r.text)

        if r.status_code == 200 and matches:
            print(f'{Fore.GREEN}Signature found:')
            print(f'{Fore.WHITE}Possible function value(s) for {signature}:')
            for match in matches:
                print(f'{Fore.YELLOW}      -{match}found!')
        elif r.status_code != 200 and not matches:
            print(
                f'{Fore.RED}Signature {signature} not found in database, returning {r.status_code}')


print(f'{Fore.WHITE}Done!')
