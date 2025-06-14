from requests import get

server_url = 'https://mobile-phone-server.vercel.app/phones'
res = get(server_url)
if res.status_code == 200:
    data = res.json()
    phones = data.get('RECORDS')



def media_from_url(img_src, phone_name):
    """
    This will return the wordpress media code from url
    """
    codes = (f'<!-- wp:image {{"sizeSlug":"large","align":"center"}} -->' \
             f'<figure class="wp-block-image aligncenter size-large">' \
             f'<img src="{img_src}" alt={phone_name} image"/>' \
             f'<figcaption class="wp-element-caption">{phone_name}</figcaption></figure>' \
             f'<!-- /wp:image -->')
    return codes

def wp_table_dic(dictionary):
    """
    This will generate wordpress gutenberg table code from dictionary
    :param: dictionary
    :return: html table string
    """
    codes = '<!-- wp:table --><figure class="wp-block-table"><table class="has-fixed-layout"><tbody>'
    for key, value in dictionary.items():
        tr_data = f'<tr><td>{key}</td><td>{value}</td></tr>'
        codes += tr_data
    codes += '</tbody></table></figure><!-- /wp:table -->'
    return codes

def wp_paragraph(text):
    """
    This will generate wordpress gutenberg paragraph code
    """
    codes = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return codes

def wp_heading_two(text):
    return f'<!-- wp:heading --> <h2 class="wp-block-heading">{text}</h2> <!-- /wp:heading -->'


for phone in phones:
    name = phone.get('name').title()
    released_at = phone.get('released_at').lower().replace('Released ', ' ')
    chipset = phone.get('chipset')
    body = phone.get('body')
    os = phone.get('os')
    picture = phone.get('picture')


    first_dictionary = {
        'name': name,
        'released_at': released_at,
        'chipset': chipset,
        'body': body
    }
    first_paragraph = (f'{name} has been released on {released_at}. ' \
                       f'It comes with {chipset}. The body of this mobile is {body}. ' \
                       f'{os} is the built-in Android version.')
    article_paragraph = wp_paragraph(first_paragraph)
    first_image = media_from_url(picture, name)
    first_heading = wp_heading_two(f'{name} Overview')
    first_table = wp_table_dic(first_dictionary)

    # specifications section
    specifications = phone.get('specifications')
    print(type(specifications))




