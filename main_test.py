import mock
import builtins
import main


def test_q1(capfd):
    input_output = {
        '7': 'O número não possui divisores multiplos de 3\n',
        '3': 'Quantidade de divisores divisiveis por 3: 1\n',
        '555':'Quantidade de divisores divisiveis por 3: 4\n',
        '3144':'Quantidade de divisores divisiveis por 3: 8\n',
        '17640':'Quantidade de divisores divisiveis por 3: 48\n'
    }
    for k, v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q1()
            out, err = capfd.readouterr()
            assert out == v
