from slackbot_helper.svc import HighlightOutputText


def test_service():

    input_text = "where is the library?"
    output_text = "I understand you want to know where the library is."

    dmo = HighlightOutputText()
    assert dmo

    result = dmo.process(
        text_1=input_text,
        text_2=output_text)

    print(result)


def main():
    test_service()


if __name__ == "__main__":
    main()
