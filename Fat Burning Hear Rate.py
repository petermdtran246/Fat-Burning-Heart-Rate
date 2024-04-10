def get_age():
    age = int(input())
    if not (18 <= age <= 75):
        raise ValueError('Invalid age.')
    return age


def fat_burning_heart_rate(age):
    max_heart_rate = 220 - age
    fat_burning_heart_rate = max_heart_rate * 0.7
    return fat_burning_heart_rate


if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print(f"Fat burning heart rate for a {age} year-old: {heart_rate:.1f} bpm")
    except ValueError as e:
        print(f'Invalid age. {e}')
        print('Could not calculate heart rate info.')

