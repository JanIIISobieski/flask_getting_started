import requests


def main():
    r1 = requests.get('http://vcm-3602.vm.duke.edu:5000/')
    print(r1.text)

    r2 = requests.get('http://vcm-3602.vm.duke.edu:5000/name')
    print(r2.json()['name'])

    r3 = requests.get('http://vcm-3602.vm.duke.edu:5000/hello/Gabriel')
    print(r3.json()['message'])

    r4 = requests.post('http://vcm-3602.vm.duke.edu:5000/distance',
                       json={'a': [2, 5], 'b': [5, 10]})
    print(r4.json())


if __name__ == '__main__':
    main()
