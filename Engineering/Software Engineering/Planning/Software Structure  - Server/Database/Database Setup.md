# Model Airport Server

## Database Structure

### airports

| Field | Type | Not Null | Key | Notes |
| :---: | :---: | :---: | :---: | :---: |
| name | varchar(70) | Yes | Primary | - |
| availability | boolean | Yes | - | - |

## Notes

### Things To Avoid

* https://www.npmjs.com/package/sql-injection
   * This library caused some sort of freeze on the application. Cause is unknown.

### Fixed Mistakes

* Removed all SQL injection prevention modules as the pg module already has parameterized queries which prevents most SQL attacks in the first place. Example of duplicate security measures.