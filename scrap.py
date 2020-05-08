from pip_lock import check_requirements, get_mismatches

m = get_mismatches('requirements.txt')

print(check_requirements('requirements.txt',post_text='\nRun the following on your host machine: \n\nvagrant provision\n'))