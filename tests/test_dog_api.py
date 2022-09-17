import allure
import pytest


@allure.feature('Random dog')
@allure.story('Get random dog image')
def test_get_random_dog(dog_api):
	response = dog_api.get('breeds/image/random')

	with allure.step('Request sended, looking at the response code'):
		assert response.status_code == 200,\
			f"Wrong response code, received {response.status_code}"

	with allure.step('Checking response status'):
		response = response.json()
		assert response['status'] == 'success'


@allure.feature('Random dog')
@pytest.mark.parametrize("breed_terrier", [
    "american",
	"australian",
	"bedlington",
	"border",
	"cairn",
	"dandie",
	"fox",
	"irish",
	"kerryblue",
	"lakeland",
	"norfolk",
	"norwich",
	"patterdale",
	"russell",
	"scottish",
	"sealyham",
	"silky",
	"tibetan",
	"toy",
	"welsh",
	"westhighland",
	"wheaten",
	"yorkshire"
])
@allure.story('Image of a random dog from a terrier breed')
def test_get_random_terrier_breed_image(dog_api, breed_terrier):
	response = dog_api.get(f'breed/terrier/{breed_terrier}/images/random')
	response = response.json()
	print(response)
	assert breed_terrier in response["message"],\
		f"No link to the dog image, response = {response}"


@allure.feature('List of dog images')
@allure.story('List of all terrier dogs images contains only images')
@pytest.mark.parametrize("file", ['.doc', '.html', '.exe', '.txt'])
def test_get_breed_images_and_check_file_type(dog_api, file):
	response = dog_api.get("breed/terrier/images")
	response = response.json()
	result = '\n'.join(response['message'])
	assert file not in result, \
		f"Founded file with the extension - {file}"


@allure.feature('List of dog images')
@pytest.mark.parametrize("breed", [
	"akita",
	"husky",
	"labrador",
	"pomeranian",
	"shiba",
	"australian",
	"collie",
	"corgi"
])
@allure.story('List of certain dog breed')
def test_get_random_breed_images(dog_api, breed):
	response = dog_api.get(f'breed/{breed}/images/')
	response = response.json()
	assert response["status"] == 'success',\
		f'Failed to get a list of images'


@allure.feature('List of dog images')
@allure.story('List certain number of random images')
@pytest.mark.parametrize('number_of_images', [i for i in range(1, 10)])
def test_get_few_sub_breed_random_images(dog_api, number_of_images):
	response = dog_api.get(f"breed/terrier/norfolk/images/random/{number_of_images}")
	response = response.json()
	final_len = len(response["message"])
	print(final_len)
	assert final_len == number_of_images,\
		f"Wrong number of photo = {number_of_images}"

