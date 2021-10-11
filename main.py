def is_prime(x):
    '''
    determina daca un numar este prim sau nu
    :param x: numar intreg
    :return: True, daca x este prim sau False in caz contrar
    '''
    if (x < 2):
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def get_largest_prime_below(n):
    """
    gaseste ultimul numar prim mai mic decat un numar dat
    :param n: numar intreg
    :return: ultimul numar prim mai mic decat n sau -1 daca nu exista un astfel de numar
    """
    if n < 3:
        return -1
    for i in range(n - 1, 1, -1):
        if is_prime(i):
            return i

def test_is_prime(self):
        """
        teste pentru functia is_prime
        """
        assert is_prime(-5) is False
        assert is_prime(1) is False
        assert is_prime(2) is True
        assert is_prime(11) is True
        assert is_prime(25) is False

def test_get_largest_prime_below(self):
        """
        teste pentru functia test_get_largest_prime_below():
        """
        assert get_largest_prime_below(2) == -1
        assert get_largest_prime_below(5) == 3
        assert get_largest_prime_below(20) == 19
        assert get_largest_prime_below(-10) == -1
        assert get_largest_prime_below(30) == 29


def is_palindrome(n):
    '''
    functia verifica daca un numar este palindrom sau nu
    :param n: numar intreg
    :return: True, daca n este palindrom sau False, in caz contrar
    '''
    copie_n = n
    oglindit_n = 0
    while n > 0:
        oglindit_n = oglindit_n * 10 + n % 10
        n = n // 10
    if copie_n == oglindit_n:
        return True
    return False



def test_is_palindrome():
        '''
        teste pentru functia is_palindrome
        '''
        assert is_palindrome(7) == True
        assert is_palindrome(12) == False
        assert is_palindrome(121) == True
        assert is_palindrome(75) == False
        assert is_palindrome(33) == True


def main():
    n = int(input("dati nr: "))
    rezultat = get_largest_prime_below(n)
    if rezultat == -1:
        print("Nu exista un astfel de numar")
    else:
        print(rezultat)
    n = int(input("dati nr: "))
    if is_palindrome(n) == True:
        print("numarul ", n, " este palindrom")
    else:
        print("numarul ", n, " NU este palindrom")

main()