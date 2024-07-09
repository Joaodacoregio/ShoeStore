from faker import Faker
from random import randint




fake = Faker("pt_BR")



def rand_ratio():
    return randint(840, 900), randint(473, 573)

def make_product(): 
    return {
        'id': randint(0,1000),
        'title': fake.sentence(nb_words=6),
        "mark": fake.word(),
        'gender': fake.random_element(elements=('Masculino', 'Feminino')),
        'category': fake.word(),
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/shoes' % rand_ratio()}
        }
 
if __name__ =="__main__":
    print(make_product())