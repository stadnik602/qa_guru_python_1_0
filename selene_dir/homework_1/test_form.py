import os

from selene import browser, be, have

DIR_PATH = os.path.dirname(os.path.abspath(__file__))

FORM_PAGE_URL = '/automation-practice-form'
# Given
first_name_field = browser.element('#firstName')
last_name_field = browser.element('#lastName')
email_field = browser.element('#userEmail')
mobile_field = browser.element('#userNumber')
date_of_birth_field = browser.element('#dateOfBirthInput')

subject_input = browser.element('#subjectsInput')
current_address_input = browser.element('#currentAddress')
choose_picture_button = browser.element('#uploadPicture')
state_input = browser.element('#react-select-3-input')
city_input = browser.element('#react-select-4-input')

submit_button = browser.element('#submit')

gender_radiobuttons = {
    'Male': browser.element('[for = "gender-radio-1"]'),
    'Female': browser.element('[for = "gender-radio-2"]'),
    'Other': browser.element('[for = "gender-radio-3"]')
}
gender_radiobuttons_2 = {
    'Male': browser.all('[for ^= "gender-radio"]').element_by(have.text('Male')),
    'Female': browser.all('[for ^= "gender-radio"]').element_by(have.text('Female')),
    'Other': browser.all('[for ^= "gender-radio"]').element_by(have.text('Other'))
}
datepicker = {
    'month_dropdown': browser.element('.react-datepicker__month-select'),
    'year_dropdown': browser.element('.react-datepicker__year-select'),
    'days': browser.element('.react-datepicker__month'),
              }

hobbies_checkboxes = {
    'Sports': browser.all('[for ^= "hobbies-checkbox"]').element_by(have.text('Sports')),
    'Reading': browser.all('[for ^= "hobbies-checkbox"]').element_by(have.text('Reading')),
    'Music': browser.all('[for ^= "hobbies-checkbox"]').element_by(have.text('Music'))
}

confirmation_popup_title_element = '#example-modal-sizes-title-lg'


def test_successes_submit_form():
    browser.open(FORM_PAGE_URL)

    # When
    first_name_field.type('Kurva')
    last_name_field.type('Bobr')
    email_field.type('kurvabobr@gmail.com')
    gender_radiobuttons.get('Female').click()
    gender_radiobuttons_2.get('Male').click()
    mobile_field.type('1234567890')
    date_of_birth_field.click()
    datepicker.get('year_dropdown').click()
    browser.element('[value="2021"]').click()
    datepicker.get('month_dropdown').click()
    browser.element('[value="3"]').click()
    browser.element('.react-datepicker__day--019').click()
    subject_input.send_keys('Com').press_enter()
    hobbies_checkboxes.get('Music').click()
    choose_picture_button.send_keys(DIR_PATH+"/robert.webp")
    current_address_input.type('202-2 Dunsheath Way')
    state_input.click()
    browser.all('[id ^= "react-select"][id *= "option"]').element_by(have.text('NCR')).click()
    # state_input.send_keys('N').press_enter()
    city_input.send_keys('no').press_enter()
    submit_button.click()

# Then
    browser.element(confirmation_popup_title_element).should(be.visible)
    browser.element(confirmation_popup_title_element).should(have.exact_text('Thanks for submitting the form'))
    print()
    browser.all('.table-responsive td:nth-child(2)').should(
        have.texts(
            'Kurva Bobr',
            'kurvabobr@gmail.com',
            'Female',
            '1234567890',
            '19 April,2021',
            'Computer Science',
            'Music',
            'robert.webp',
            '202-2 Dunsheath Way',
            'NCR Noida'
        )
    )
