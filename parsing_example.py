from html.parser import HTMLParser

class CustomHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tag_flag = False
        self.tag_line_num = 0
        self.tag_string = 'temporary_tag'
        
    def initiate_vars(self, tag_string):
        self.tag_string = tag_string
        
    def handle_starttag(self, tag, attrs):
        #if tag == 'tag_to_search_for':
        if tag == self.tag_string:
            self.tag_flag = True
            self.tag_line_num = self.getpos()


if __name__== '__main__':
    simple_str = 'string_to_search_for'
    parser_obj = CustomHTMLParser()
    #parser_obj.initiate_vars('tag_to_search_for')
    parser_obj.initiate_vars('hr')

    html_file = open('location_of_html_file//file.html')
    html_str = html_file.read()

    html_search_result = html_str.find(simple_str)
    if html_search_result != -1:
        print ('The word {} was found'.format(simple_str))
    
    parser_obj.feed(html_str)

    if parser_obj.tag_flag:
        print ('Tag {0} was found at position {1}'.format(parser_obj.tag_string, parser_obj.tag_line_num))
    else:
        print ('Tag {} was not found'.format(parser_obj.tag_string))
        
        
            
            
    
