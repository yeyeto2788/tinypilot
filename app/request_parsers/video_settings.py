from request_parsers import errors
from request_parsers import message as message_parser


def parse_fps(request):
    message = message_parser.parse_message(request,
                                           required_fields=['videoFps'])
    try:
        # Note: We need to cast the value to a string first otherwise the int
        # function forces floats into integers by simply cutting off the
        # fractional part. This results in the value being incorrectly
        # validated as an integer.
        video_fps = int(str(message['videoFps']))
        if not 1 <= video_fps <= 30:
            raise ValueError
    except ValueError as e:
        raise errors.InvalidVideoFpsError(
            'The video FPS must be an whole number between 1 and 30.') from e
    return video_fps


def parse_jpeg_quality(request):
    message = message_parser.parse_message(request,
                                           required_fields=['videoJpegQuality'])
    try:
        # Note: We need to cast the value to a string first otherwise the int
        # function forces floats into integers by simply cutting off the
        # fractional part. This results in the value being incorrectly
        # validated as an integer.
        video_jpeg_quality = int(str(message['videoJpegQuality']))
        if not 1 <= video_jpeg_quality <= 100:
            raise ValueError
    except ValueError as e:
        raise errors.InvalidVideoJpegQualityError(
            'The video JPEG quality must be an whole number between 1 and 100.'
        ) from e
    return video_jpeg_quality
