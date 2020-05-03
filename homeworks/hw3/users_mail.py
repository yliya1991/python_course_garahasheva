from faker import Faker

def user_list(count, int=100):
    fake = Faker()
    text = ''
    
    for i in range(count):
        text += (fake.name() + ' ' + fake.email() + '\n')
    return text