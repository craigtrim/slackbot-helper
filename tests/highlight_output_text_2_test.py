from slackbot_helper.core.svc import HighlightOutputText


def test_service_1():

    input_text = "where is the library?"
    output_text = "I understand you want to know where the library is."

    dmo = HighlightOutputText()
    assert dmo

    result = dmo.process(
        text_1=input_text,
        text_2=output_text)

    print(result)
    assert result == "I understand you want to know *where the library is.*"


def test_service_2():

    input_text = "please help me find the library"
    output_text = "I understand you want to know where the library is."

    dmo = HighlightOutputText()
    assert dmo

    result = dmo.process(
        text_1=input_text,
        text_2=output_text)

    assert not result


def main():
    test_service_1()


if __name__ == "__main__":
    main()
