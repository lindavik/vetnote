from vetnote.main import main


def test_main(capsys):
    expected_output: str = "Welcome to VetNote"

    main()

    actual_output = capsys.readouterr()

    assert expected_output in actual_output.out
