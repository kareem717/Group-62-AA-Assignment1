# Requirement 1: Index Page To Authentication Redirect

## Test Case: Redirect to Login

**Objective:**  
To verify that the "Login" button on the `/index` page correctly redirects to the `/login` page.

**Action:**

1. Navigate to the base app URL.
2. Click on the "Login" button.

**Assert:**

- The user is redirected to the `/login` page.
- Verify that the user login form is properly displayed.
- Verify that the "Login" button is properly displayed.

## Test Case: Redirect to Register

**Objective:**  
To verify that the "Sign up" button on the `/index` page correctly redirects to the `/sign-up` page.

**Action:**

1. Navigate to the base app URL.
2. Click on the "Sign up" button.

**Assert:**

- The user is redirected to the `/sign-up` page.
- Verify that the user registration form is properly displayed.
- Verify that the "Sign up" button is properly displayed.

# Requirement 2: User Registration

**Note**
A valid email is defined as the following:

- In the form of: {locale}@{domain}.{tld}.
- Maximum total length of 320, minimum total length of 6
- Maximum locale length of 64, minimum length of 1
- Maximum domain length of 191, minimum length of 1
- Maximum TLD length of 63, minimum length of 2

A valid password is defined as the following:

- Between 6-320 characters (inclusive.)
- Any character type.

## Test Case: Invalid Email Form Error

**Objective:**  
Verify form is being verified on and displaying correct form errors on the invalid input.

**Action:**

1. Navigate to `/sign-up` page.
2. Input a invalid (falls out of any part of the definition) email.
3. Input a valid password.
4. Press "Sign up" button.

**Assert:**

- No form error present on the password field.
- A "Invalid email" form error is present on the email field.
- No redirect occurs

## Test Case: Password Too Short Form Error

**Objective:**  
Verify form is being verified on and displaying correct form errors on the invalid input.

**Action:**

1. Navigate to `/sign-up` page.
2. Input a valid email.
3. Input a invalid (5 or less characters) password.
4. Press "Sign up" button.

**Assert:**

- No form error present on the email field.
- A "Too short" form error is present on the password field.
- No redirect occurs

## Test Case: Password Too Long Form Error

**Objective:**  
Verify form is being verified on and displaying correct form errors on the invalid input.

**Action:**

1. Navigate to `/sign-up` page.
2. Input a valid email.
3. Input a invalid (321 or more characters) password.
4. Press "Sign up" button.

**Assert:**

- No form error present on the email field.
- A "Too long" form error is present on the password field.
- No redirect occurs

## Test Case: Redirect on Register

**Objective:**  
Verify that you are redirected on a valid registration.

**Action:**

1. Navigate to `/sign-up` page.
2. Input a valid email.
3. Input a valid password.
4. Press "Sign up" button.

**Assert:**

- No form errors are present.
- User is correctly redirected to the `/login` page.
- Verify that the user login form is properly displayed.
- Verify that the "Login" button is properly displayed.
