from faker import Faker

def users_list(count: int=100):
    fake = Faker()
    result = ''

    for i in range(count):
        result+=(fake.name()+' '+fake.email()+ '\n')
        
    return result
