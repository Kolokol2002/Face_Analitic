from deepface import DeepFace

def face_analitic(image):
    try:
        result = DeepFace.analyze(img_path=image, actions= ('emotion', 'age', 'gender', 'race'))
        print(f'Вік: {result["age"]}')
        print(f'Стать: {result["gender"]}')
        print(f'Емоції:')
        for i, n in result.get('emotion').items():
            print(f'    {i} - {round(n, 1)}%')
        print(f'Расса:')
        for i, n in result.get('race').items():
            print(f'    {i} - {round(n, 1)}%')
    except Exception as exc:
        print(exc)

def main():
    face_analitic(image="img_4.png")

if __name__ == '__main__':
    main()