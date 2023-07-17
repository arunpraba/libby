# Libby Project

## Description

This project is to learn Django & graphql.

<!-- Update installation based on Pipfile -->

## Installation

```bash
pipenv install
```

## Auth mutations

### Create user

```gql
mutation CreateUser {
  userCreate(email: "john@gmail.com", password: "password", username: "john") {
    user {
      id
      username
      firstName
      lastName
      email
    }
  }
}
```

### Login

```gql
mutation Login {
  login(username: "tom", password: "password") {
    payload
    refreshExpiresIn
    token
  }
}
```

### Refresh token

```gql
mutation RefreshToken {
  refreshToken(token: "token") {
    payload
    refreshExpiresIn
    token
  }
}
```
