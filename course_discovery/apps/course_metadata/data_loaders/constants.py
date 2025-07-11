"""
Various constants across different data loaders.
"""


class CSVIngestionErrors:
    """
    Enumerate errors possible during CSVLoader ingestion.
    """
    MISSING_ORGANIZATION = 'MISSING_ORGANIZATION'
    MISSING_COURSE_TYPE = 'MISSING_COURSE_TYPE'
    MISSING_COURSE_RUN_TYPE = 'MISSING_COURSE_RUN_TYPE'
    MISSING_REQUIRED_DATA = 'MISSING_REQUIRED_DATA'
    COURSE_CREATE_ERROR = 'COURSE_CREATE_ERROR'
    COURSE_RUN_CREATE_ERROR = 'COURSE_RUN_CREATE_ERROR'
    IMAGE_DOWNLOAD_FAILURE = 'IMAGE_DOWNLOAD_FAILURE'
    LOGO_IMAGE_DOWNLOAD_FAILURE = 'LOGO_IMAGE_DOWNLOAD_FAILURE'
    COURSE_UPDATE_ERROR = 'COURSE_UPDATE_ERROR'
    COURSE_RUN_UPDATE_ERROR = 'COURSE_RUN_UPDATE_ERROR'
    COURSE_RUN_NOT_FOUND = 'COURSE_RUN_NOT_FOUND'
    COURSE_NOT_FOUND = 'COURSE_NOT_FOUND'


class CSVIngestionErrorMessages:
    """
    String templates for various CSV ingestion error messages.
    """
    MISSING_ORGANIZATION = '[MISSING_ORGANIZATION] Unable to locate partner organization with key {org_key} ' \
                           'for the course titled {course_title}.'

    MISSING_COURSE_TYPE = '[MISSING_COURSE_TYPE] Unable to find the course enrollment track "{course_type}"' \
                          ' for the course {course_title}'

    MISSING_COURSE_RUN_TYPE = '[MISSING_COURSE_RUN_TYPE] Unable to find the course run enrollment track' \
                              ' "{course_run_type}" for the course {course_title}'

    MISSING_REQUIRED_DATA = '[MISSING_REQUIRED_DATA] Course {course_title} is missing the required data for ' \
                            'ingestion. The missing data elements are "{missing_data}"'

    COURSE_CREATE_ERROR = '[COURSE_CREATE_ERROR] Unable to create course {course_title} in the system. The ingestion ' \
                          'failed with the exception: {exception_message}'

    COURSE_RUN_CREATE_ERROR = '[COURSE_RUN_CREATE_ERROR] Unable to create course run of the course {course_title} ' \
                              'with variant_id {variant_id} in the system. The ingestion failed with the exception: ' \
                              '{exception_message}'

    COURSE_UPDATE_ERROR = '[COURSE_UPDATE_ERROR] Unable to update course {course_title} in the system. The update ' \
                          'failed with the exception: {exception_message}'

    COURSE_ENTITLEMENT_PRICE_UPDATE_ERROR = '[COURSE_ENTITLEMENT_PRICE_UPDATE_ERROR] Unable to update ' \
                                            'course entitlement price for the course {course_title} in the system. ' \
                                            'The update failed with the exception: {exception_message}'

    COURSE_RUN_UPDATE_ERROR = '[COURSE_RUN_UPDATE_ERROR] Unable to update course run of the course {course_title} ' \
                              'in the system. The update failed with the exception: {exception_message}'

    IMAGE_DOWNLOAD_FAILURE = '[IMAGE_DOWNLOAD_FAILURE] The course image download failed for the course' \
                             ' {course_title}.'

    LOGO_IMAGE_DOWNLOAD_FAILURE = '[LOGO_IMAGE_DOWNLOAD_FAILURE] The logo image download failed for the course ' \
                                  '{course_title}.'


CSV_LOADER_ERROR_LOG_SEQUENCE = [
    CSVIngestionErrors.MISSING_ORGANIZATION, CSVIngestionErrors.MISSING_COURSE_TYPE,
    CSVIngestionErrors.MISSING_COURSE_RUN_TYPE, CSVIngestionErrors.MISSING_REQUIRED_DATA,
    CSVIngestionErrors.IMAGE_DOWNLOAD_FAILURE, CSVIngestionErrors.LOGO_IMAGE_DOWNLOAD_FAILURE,
    CSVIngestionErrors.COURSE_CREATE_ERROR, CSVIngestionErrors.COURSE_UPDATE_ERROR,
    CSVIngestionErrors.COURSE_RUN_UPDATE_ERROR, CSVIngestionErrors.COURSE_RUN_NOT_FOUND,
    CSVIngestionErrors.COURSE_RUN_CREATE_ERROR, CSVIngestionErrors.COURSE_NOT_FOUND
]


class CourseEditorIngestionErrors:
    """
    Error codes for CourseEditorsLoader ingestion failures.
    """
    USER_NOT_FOUND = 'USER_NOT_FOUND'
    USER_ORG_MISMATCH = 'USER_ORG_MISMATCH'
    COURSE_NOT_FOUND = 'COURSE_NOT_FOUND'
    MISSING_REQUIRED_DATA = 'MISSING_REQUIRED_DATA'
    COURSE_EDITOR_ADD_ERROR = 'COURSE_EDITOR_ADD_ERROR'
    COURSE_EDITOR_REMOVE_ERROR = 'COURSE_EDITOR_REMOVE_ERROR'
    UNSUPPORTED_ACTION = 'UNSUPPORTED_ACTION'


class CourseEditorIngestionErrorMessages:
    """
    Error message templates for CourseEditorsLoader ingestion.
    """
    USER_NOT_FOUND = '[USER_NOT_FOUND] [Row {index}] Unable to find user with identifier "{user_identifier}".'
    USER_ORG_MISMATCH = (
        '[USER_ORG_MISMATCH] [Row {index}] User "{user_identifier}" does not belong to any '
        'authoring organization for course "{course_title}".'
    )
    COURSE_NOT_FOUND = '[COURSE_NOT_FOUND] [Row {index}] Unable to find course with identifier "{course_identifier}".'
    MISSING_REQUIRED_DATA = '[MISSING_REQUIRED_DATA] [Row {index}] Missing required field(s): {missing_fields}'
    COURSE_EDITOR_ADD_ERROR = (
        '[COURSE_EDITOR_ADD_ERROR] [Row {index}] Failed to create CourseEditor for user '
        '"{user_identifier}" and course "{course_title}": {exception}'
    )
    COURSE_EDITOR_REMOVE_ERROR = (
        '[COURSE_EDITOR_REMOVE_ERROR] [Row {index}] Failed to remove CourseEditor for user '
        '"{user_identifier}" and course "{course_title}": {exception}'
    )
    UNSUPPORTED_ACTION = "[UNSUPPORTED_ACTION] [Row {index}] Unsupported action '{action}' for course editor."


COURSE_EDITOR_LOADER_ERROR_LOG_SEQUENCE = [
    CourseEditorIngestionErrors.MISSING_REQUIRED_DATA,
    CourseEditorIngestionErrors.USER_NOT_FOUND,
    CourseEditorIngestionErrors.USER_ORG_MISMATCH,
    CourseEditorIngestionErrors.COURSE_EDITOR_ADD_ERROR,
    CourseEditorIngestionErrors.COURSE_NOT_FOUND,
    CourseEditorIngestionErrors.COURSE_EDITOR_REMOVE_ERROR,
    CourseEditorIngestionErrors.UNSUPPORTED_ACTION
]


class DegreeCSVIngestionErrors:
    """
    Possible errors that will raise during Degree CSV Loader ingestion flow.
    """
    MISSING_REQUIRED_DATA = 'MISSING_REQUIRED_DATA'
    MISSING_ORGANIZATION = 'MISSING_ORGANIZATION'
    MISSING_PROGRAM_TYPE = 'MISSING_PROGRAM_TYPE'
    MISSING_SUBJECT_DATA = 'MISSING_SUBJECT_DATA'
    MISSING_LEVEL_TYPE_DATA = 'MISSING_LEVEL_TYPE_DATA'
    MISSING_LANGUAGE_TAG_DATA = 'MISSING_LANGUAGE_TAG_DATA'
    DEGREE_CREATE_ERROR = 'DEGREE_CREATE_ERROR'
    DEGREE_UPDATE_ERROR = 'DEGREE_UPDATE_ERROR'
    IMAGE_DOWNLOAD_FAILURE = 'IMAGE_DOWNLOAD_FAILURE'
    LOGO_IMAGE_DOWNLOAD_FAILURE = 'LOGO_IMAGE_DOWNLOAD_FAILURE'


class DegreeCSVIngestionErrorMessages:
    """
    String templates for various CSV ingestion error messages.
    """
    MISSING_ORGANIZATION = '[MISSING_ORGANIZATION] Unable to locate partner organization with key {} ' \
                           'for the degree {degree_slug}.'

    MISSING_PROGRAM_TYPE = '[MISSING_PROGRAM_TYPE] Unable to find the program type "{}" ' \
                           'for the degree {degree_slug}'

    MISSING_REQUIRED_DATA = '[MISSING_REQUIRED_DATA] Degree {degree_slug} is missing the required data for ' \
                            'ingestion. The missing data elements are "{missing_data}"'

    MISSING_SUBJECT_DATA = '[MISSING_SUBJECT_DATA] Unable to find the subject "{}" ' \
                           'for the degree {degree_slug}'

    MISSING_LEVEL_TYPE_DATA = '[MISSING_LEVEL_TYPE_DATA] Unable to find the level type "{}" ' \
                              'for the degree {degree_slug}'

    MISSING_LANGUAGE_TAG_DATA = '[MISSING_LANGUAGE_TAG_DATA] Unable to find the language "{}" ' \
                                'for the degree {degree_slug}'

    DEGREE_CREATE_ERROR = '[DEGREE_CREATE_ERROR] Unable to create degree {degree_slug} in the system. The ingestion' \
                          'failed with the exception: {exception_message}'

    DEGREE_UPDATE_ERROR = '[DEGREE_UPDATE_ERROR] Unable to update degree {degree_slug} in the system. The update' \
                          'failed with the exception: {exception_message}'

    IMAGE_DOWNLOAD_FAILURE = '[IMAGE_DOWNLOAD_FAILURE] The degree image download failed for the degree' \
                             ' {degree_slug}.'

    LOGO_IMAGE_DOWNLOAD_FAILURE = '[LOGO_IMAGE_DOWNLOAD_FAILURE] The logo image download failed for the degree ' \
                                  '{degree_slug}.'


DEGREE_LOADER_ERROR_LOG_SEQUENCE = [
    DegreeCSVIngestionErrors.MISSING_REQUIRED_DATA, DegreeCSVIngestionErrors.MISSING_ORGANIZATION,
    DegreeCSVIngestionErrors.MISSING_PROGRAM_TYPE, DegreeCSVIngestionErrors.MISSING_SUBJECT_DATA,
    DegreeCSVIngestionErrors.MISSING_LEVEL_TYPE_DATA, DegreeCSVIngestionErrors.MISSING_LANGUAGE_TAG_DATA,
    DegreeCSVIngestionErrors.DEGREE_CREATE_ERROR, DegreeCSVIngestionErrors.DEGREE_UPDATE_ERROR,
    DegreeCSVIngestionErrors.IMAGE_DOWNLOAD_FAILURE, DegreeCSVIngestionErrors.LOGO_IMAGE_DOWNLOAD_FAILURE
]
