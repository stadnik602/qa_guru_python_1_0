import os

from selene import browser, be, have, command

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
state_dropdown_elements = browser.all('[id ^= "react-select"][id *= "option"]')
city_dropdown_elements = browser.all('[id ^= "react-select"][id *= "option"]')

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
    datepicker.get('year_dropdown').send_keys('2022')
    datepicker.get('month_dropdown').send_keys('April')
    browser.element('.react-datepicker__day--019').click()
    subject_input.send_keys('Com').press_enter()
    hobbies_checkboxes.get('Music').click()
    # choose_picture_button.send_value(os.path.abspath(os.path.join(os.path.dirname(tests.__file__),"resources/robert.webp")))
    choose_picture_button.send_keys(DIR_PATH+"/resources/robert.webp")
    current_address_input.type('202-2 Dunsheath Way')
    '''    current_address_input.with_(set_value_by_js=True).set_value('202-2 Dunsheath Way')
    current_address_input.perform(command.js.set_value('202-2 Dunsheath Way'))'''
    state_input.perform(command.js.scroll_into_view)

    state_input.perform(command.js.click)
    state_input.click()
    # state_dropdown_elements.element_by(have.text('NCR')).click()
    city_input.click()
    city_dropdown_elements.element_by(have.text('Noida')).click()

    submit_button.perform(command.js.scroll_into_view)
    submit_button.click()

    # Then
    browser.element(confirmation_popup_title_element).should(be.visible)
    browser.element(confirmation_popup_title_element).should(have.exact_text('Thanks for submitting the form'))
    browser.element(confirmation_popup_title_element).should(have.exact_text('Thanks for submitting the form'))
    '''browser.element('.table').all('td').even.should(
        have.texts(
            'Kurva Bobr',
            'kurvabobr@gmail.com',
            'Male',
            '1234567890',
            '19 April,2022',
            'Computer Science',
            'Music',
            'robert.webp',
            '202-2 Dunsheath Way',
            'NCR Noida',
        ))'''
    browser.all('.table').all('td').should(
        have.texts(
            ('Student Name', 'Kurva Bobr'),
            ('Student Email','kurvabobr@gmail.com'),
            ('Gender','Male'),
            ('Mobile','1234567890'),
             ('Date of Birth','19 April,2022'),
              ('Subjects','Computer Science'),
               ('Hobbies','Music'),
                ('Picture','robert.webp'),
                 ('Address','202-2 Dunsheath Way'),
                  ('State and City','NCR Noida')
        )
    )

'''    browser.all('.table td:nth-child(2)').should(
        have.texts(
            'Kurva Bobr',
            'kurvabobr@gmail.com',
            'Male',
            '1234567890',
            '19 April,2022',
            'Computer Science',
            'Music',
            'robert.webp',
            '202-2 Dunsheath Way',
            'NCR Noida'
        )
    )'''
