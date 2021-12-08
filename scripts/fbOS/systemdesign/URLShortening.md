# URL Shortening

---
---

## Problem Statement

## Functional Requirements

- Given a URL, our service should generate a shorter and unique alias of it. This is called a short link. This link should be short enough to be easily copied and pasted into applications.
- When users access a short link, our service should redirect them to the original link.
- Users should optionally be able to pick a custom short link for their URL.
- Links will expire after a standard default time-span. Users should be able to specify the expiration time.

## Non Functional Requirements

- The system should be highly available. This is required because, if our service is down, all the URL redirection will start failing.
- URL redirection should happen in real-time with minimal latency.
- Shortened links should not be guessable (not predictable).

## Extended Requirements

- Analytics; e.g., how many times a redirection happened?
- Our service should also be accessible through REST APIs by other services.

## Back of the Envelope Calculations

### Traffic estimates

Assuming, we will have `500M` new URL shortenings per month, with `100:1 read/write ratio`, we can expect `50 Billion` redirection during the same period:

`100 * 500 Million => 50 Billion`

QPS : `500 million / (30 days * 24 hours * 3600 seconds) = ~200 URLs/s`

URLs redirection per second : `100 * 200 URLs/s = 20K/s`

### Storage estimates

The total number of objects we expect to store for 5 years:
`500 million * 5 years * 12 months = 30 billion`

storage: `30 billion * 500 bytes = 15 TB`

### Bandwidth estimates

total incoming data: `200 * 500 bytes = 100 KB/s`

For read requests: `20K * 500 bytes = ~10 MB/s`

### Memory estimates

If we follow the 80-20 rule, meaning 20% of URLs generate 80% of traffic, we would like to cache these 20% hot URLs.

we have 20K requests per second, we will be getting 1.7 billion requests per day: `20K * 3600 seconds * 24 hours = ~1.7 billion`

cache 20% of these requests, we will need 170GB of memory.
`0.2 * 1.7 billion * 500 bytes = ~170GB`

### High-level estimates

Assuming 500 million new URLs per month and 100:1 read:write ratio

| Types  | Time  |
|---|---|
| New Urls  |  200/s |
| URL redirection  | 20 K/s  |
| Incoming Data  | 100 KB/s  |
| Outgoing Data  | 10 MB/s |
| Storage for 5 years  | 15 TB  |
| Memory for Cache  | 170 GB  |

## API design

`createURL(api_dev_key, original_url, custom_alias=None, user_name=None, expire_date=None)`

### Parameters

**api_dev_key (string)**: The API developer key of a registered account. This will be used to, among other things, throttle users based on their allocated quota.
**original_url (string)**: Original URL to be shortened.
**custom_alias (string)**: Optional custom key for the URL.
**user_name (string)**: Optional user name to be used in the encoding.
**expire_date (string)**: Optional expiration date for the shortened URL.

### Returns: (string)

A successful insertion returns the shortened URL; otherwise, it returns an error code.

`deleteURL(api_dev_key, url_key)`

Where “url_key” is a string representing the shortened URL to be retrieved; a successful deletion returns ‘URL Removed’.

### How do we detect and prevent abuse?

To prevent abuse, we can limit users via their api_dev_key. Each api_dev_key can be limited to a certain number of URL creations and redirection per some time period (which may be set to a different duration per developer key).

## Data Model

|   URL |   |
|---|---|
| PK  | Hash: varchar(16)  |
| Original URL  | varchar(512)  |
| Creation Date  | datetime  |
| Expiration Date  | datetim  |
| User ID  | int  |

| USER  |   |
|---|---|
| PK  | UserID: Int  |
| Name  | varchar(20)  |
| Email  | varchar(32)  |
| Creation  | datetime  |
| Last Login  | datetime  |


## High level design

## Detailed design

## Bottlenecks and tradeoffs
