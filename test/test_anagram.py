from anagram import main


def test_case_1(capsys):
    main(['This', 'domain', 'is', 'established', 'to', 'be', 'used', 'for',
          'illustrative', 'examples', 'in', 'documents'])

    captured = capsys.readouterr()
    assert captured.out == 'Thsi doiman is ethssbieadl to be uesd for ' \
        + 'iaseltlviutr eaesplxm in duntsoecm \n'
