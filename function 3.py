def weather(month_name):
    if month_name == 'july':
        print('winter')
    if month_name =='september':
        print('autumn')
    if month_name == 'january':
        print('spring')


month=input("enter month name between july september and january: ").lower()
weather(month)