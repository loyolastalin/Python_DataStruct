def htmlTag(msg):
    message = msg
    
    def content(value):
        return message, value
        
    return content

htmlContent = htmlTag('i')
print(htmlContent('sdas'))
print(htmlContent('sdas'))


    
    
    