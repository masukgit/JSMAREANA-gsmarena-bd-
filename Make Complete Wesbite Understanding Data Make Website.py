import base64
from requests import get, post
import json


wp_user = 'masuk11'
wp_pass = 'bVhE U4LD P7va 7guR XVvo Uhr4'
wp_credential = f'{wp_user}:{wp_pass}'
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {
    'Authorization': f'Basic {wp_token.decode('utf-8')}',
    'User-Agent': 'Firefox/5.0'
}

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

def concatenate_string(*args):
    final = ''
    for arg in args:
        final += arg
    return final

def slugify(name):
    codes = name.strip().replace(' ', '-')
    return codes

def create_wp_post(title, content, slug):
    wp_url = 'https://ananyaskitchen.infy.uk/wp-json/wp/v2/posts'
    data = {
        'title': title,
        'content': content,
        'slug': slug
    }
    response = post(wp_url, headers=wp_headers, json=data)
    if response.status_code in [200, 201]:
        print(f'{title} is posted successfully.')
    else:
        print(f'Failed to post {title}. Status code: {response.status_code}')



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
    second_heading = wp_heading_two('Specification')
    specifications_string = phone.get('specifications')
    specifications = json.loads(specifications_string)
    second_table = wp_table_dic(specifications)

    content = concatenate_string(article_paragraph, first_image, first_heading, first_table, second_heading, second_table)
    slug = slugify(name)
    create_wp_post(name, content, slug)