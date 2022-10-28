from slackbot_helper.svc import HighlightOutputText


def test_service():

    input_text = "What is the earliest known age of fossils?"
    output_text = "The earliest known age of fossils is 3.7 billion years old."

    dmo = HighlightOutputText()
    assert dmo

    result = dmo.process(
        text_1=input_text,
        text_2=output_text)

    print(result)

    # demonstrate the asterisks around 'The earliest known age of fossils'
    assert result == "*The earliest known age of fossils* is 3.7 billion years old."


def main():
    test_service()


if __name__ == "__main__":
    main()
