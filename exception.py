try:
    number =0
    #raise ValueError('sdfsdfsd')
    error = 10/ number
except (TypeError , ValueError ) as e:
    print('error', e)
except Exception as e:
  print('hello error', e)
finally:
    print('completed')
