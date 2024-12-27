from connectivity import Connectivity
from person import Person
from bson.objectid import ObjectId





#Auxiliary methods
def person_creation() -> Person:

    try:
        age:int = int(input('Insert your age: '))

    except:
        print('You must write a number')
        return person_creation()

    name:str = input('Insert your name: ')
    email:str = input('Insert your email: ')
    phoneNumber:str = input('Insert your phone number: ')

    return Person(age, email, name, phoneNumber)

def choose_field(fields:str, numbers:list[int]) -> int:
    #fields is supposed to be a string for showing options
    #and numbers are the numbers correlating to the options in fields

    result:str
    try:
        result = int(input(fields))

    except:
        print('Invalid input, you must insert a number\n')
        return choose_field(fields, numbers)

    if (numbers.__contains__(result)):
        return result

    print(f'Invalid input, {result} is not an option.')
    return choose_field(fields, numbers)

def field_condition(field:str) -> dict:
    '''
    Here the conditions to find a certain value will be the following:
    
    exact equal
    greater than/greater than or equal to
    less than/less than or equal to

    using conditional operators such as $and, $or would be a pain in the butt for testing/using
    most because of the time needed to setup those
    (tbh this would be much less of a pain if I used GUI)
    
    that said, I wont use conditional operators, and neither will I have the patience to format more than one comparison
    '''
    
    options:str = f'{'-' *10}\nChoose the type of comparison for the field {field}:\n\n1 - equal\n2 - greater than\n3 - greater than or equal to\n4 - less than\n5 - less than or equal to\n-1 - End selection.\n{'-' *10}\nYour option: '

    condition_dict:dict = {}

    blacklist:bool = ['_id', 'name', 'email', 'phoneNumber'].__contains__(field)
    result:int = choose_field(options, [-1, 1, 2, 3, 4, 5])

    if result == -1:
        print('Comparison selection Ended.')

    elif result == 1:
        value:str
        if blacklist:
            value = input('Type the exact value you\'re looking for: ')
            if field == '_id':
                value = ObjectId(value)

        else:
            value:int = int(input('Type the exact value you\'re looking for: '))

        condition_dict.update({field:value})

    elif result == 2:
        value:int
        if not blacklist:
            value = int(input(f'The value of {field} must be greater than: '))

            condition_dict.update({field:{'$gt':value}})

        else:
            print(f'The field {field} does not support greater than operations')
            return field_condition(field)
        
    elif result == 3:
        value:int
        if not blacklist:
            value = int(input(f'The value of {field} must be greater than or equal to: '))

            condition_dict.update({field:{'$gte':value}})

        else:
            print(f'The field {field} does not support greater than or equal to operations')
            return field_condition(field)
        
    elif result == 4:
        value:int
        if not blacklist:
            value = int(input(f'The value of {field} must be less than: '))
            
            condition_dict.update({field:{'$lt':value}})

        else:
            print(f'The field {field} does not support less than operations')
            return field_condition(field)
        
    elif result == 5:
        value:int
        if not blacklist:
            value = int(input(f'The value of {field} must be less than or equal to: '))

            condition_dict.update({field:{'$lte':value}})

        else:
            print(f'The field {field} does not support less than operations')
            return field_condition(field)
    
    return condition_dict

def query_buider() -> dict:
    options:str = f'{'-' *10}\nChoose the target field to build a condition:\n\n1 - _id\n2 - name\n3 - age\n4 - email\n5 - phone number\n-1 - End selection\n{'-' *10}\nYour option: '
    
    query_dict:dict = {}
    blacklist:list = []

    while True:
        result:int = choose_field(options, [-1, 1, 2, 3, 4, 5])

        if result == -1:
            print('Selection ended.')
            break

        elif result == 1 and not blacklist.__contains__(1):
            query_dict.update(field_condition('_id'))
            blacklist.append(1)

        elif result == 2 and not blacklist.__contains__(2):
            query_dict.update(field_condition('name'))
            blacklist.append(2)

        elif result == 3 and not blacklist.__contains__(3):
            query_dict.update(field_condition('age'))
            blacklist.append(3)

        elif result == 4 and not blacklist.__contains__(4):
            query_dict.update(field_condition('email'))
            blacklist.append(4)

        elif result == 5 and not blacklist.__contains__(5):
            query_dict.update(field_condition('phoneNumber'))
            blacklist.append(5)

        elif blacklist:
            print(f'The field assigned to the number {result} can only be chosen once.')

        print(query_dict)
        
    return query_dict

def proj_dict_switch(proj_dict:dict, field:str) -> None:

    if (not proj_dict.get(field)):
        proj_dict.update({field: not proj_dict.get(field)})

    else:
        proj_dict.update({field: False})

def projection_builder() -> dict:
    options:str = f'{'-' *10}\nChoose the fields that will not show up:\n\n1 - _id\n2 - name\n3 - age\n4 - email\n5 - phone number\n6 - date of registration\n-1 - End selection\n{'-' *10}\nYour option: '
    
    projection_dict:dict = {}

    while True:
        result:int = choose_field(options, [-1, 1, 2, 3, 4, 5, 6])

        if result == -1:
            print('Selection ending.')
            break

        elif result == 1:
            proj_dict_switch(projection_dict, '_id')

        elif result == 2: 
            proj_dict_switch(projection_dict, 'name')

        elif result == 3:

            proj_dict_switch(projection_dict, 'age')

        elif result == 4:
            proj_dict_switch(projection_dict, 'email')

        elif result == 5:
            proj_dict_switch(projection_dict, 'phoneNumber')

        elif result == 6:
            proj_dict_switch(projection_dict, 'registration_date')


        print(f'{'-' *10}\n{projection_dict}\n')
    
    return projection_dict

def set_unset(field:str) -> dict:
    options:str = f'{'-' *10}\nSelect what do you want to do with this field:\n\n1 - change value\n2 - unset value\n{'-' *10}\nYour option: '

    result:int = choose_field(options, [1, 2])

    if result == 1:
        value:str = input(f'Insert your new {field}: ')
        return {'$set':{field:value}}
    
    if result == 2:
        #not unsetting here because it causes for the field to completely vanish, not even null appears
        return {'$set':{field:None}}

def update_builder() -> dict:
    options:str = f'{'-' *10}\nChoose which field is your target to change:\n\n1 - name\n2 - phone number\n3 - email\n-1 - End selection\n{'-' *10}\nYour option: '
    
    update_dict:dict = {}
    blacklist:list = []

    while True:
        result:int = choose_field(options, [-1, 1, 2, 3])

        if result == -1:
            print('Selection ended.')
            break

        elif result == 1 and not blacklist.__contains__(1):
            update_dict.update(set_unset('name'))
            blacklist.append(1)

        elif result == 2 and not blacklist.__contains__(2):
            update_dict.update(set_unset('phoneNumber'))
            blacklist.append(2)

        elif result == 3 and not blacklist.__contains__(3):
            update_dict.update(set_unset('email'))
            blacklist.append(3)

        elif blacklist:
            print(f'The field assigned to the number {result} can only be chosen once.')

    return update_dict





def create(collection) -> None:
    person:Person = person_creation()
    Connectivity.insert_one(collection, person)

def read(collection) -> None:
    query:dict = query_buider()
    projection:dict = projection_builder()
    result:list = Connectivity.find(collection, query, projection)
    print(result)

def update_one(collection) -> None:
    query:dict = query_buider()
    values:dict = update_builder()
    Connectivity.update_one(collection, query, values)

def update_many(collection) -> None:
    query:dict = query_buider()
    values:dict = update_builder()
    Connectivity.update_many(collection, query, values)

def delete(collection) -> None:
    query:dict = query_buider()
    Connectivity.delete_one(collection, query)





client = Connectivity.get_client('mongodb://localhost:27017/')
db = Connectivity.get_db(client, 'simpleCrud')
collection = Connectivity.get_collection(db, 'simpleCrud')

options = f'{'-'*10}\n1 - Create\n2 - Read\n3 - Update_One\n4 - Update_Many\n5 - Delete_One\n-1 - End program\n{'-'*10}\nYour option: '

while True:
    result:int = choose_field(options, [-1, 1, 2, 3, 4, 5])

    if result == -1:
        print('Program ended.')
        break

    elif result == 1:
        create(collection)

    elif result == 2:
        read(collection)

    elif result == 3:
        update_one(collection)

    elif result == 4:
        update_many(collection)

    elif result == 5:
        delete(collection)