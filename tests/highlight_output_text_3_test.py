from slackbot_helper.core.svc import HighlightOutputText


def test_service_1():

    input_text = "where is the location of the library"
    output_text = "so you want to know where the library is, correct?"

    dmo = HighlightOutputText()
    assert dmo

    result = dmo.process(
        text_1=input_text,
        text_2=output_text)

    print(result)


def main():
    test_service_1()


if __name__ == "__main__":
    main()
