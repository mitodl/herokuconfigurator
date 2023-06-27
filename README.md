This is a Concourse CI resource to read a YAML file as input
and set a series of Heroku configuration variables.

The variables as well as the application's name are specified
in the YAML file. Here's an example:

```yaml
---
heroku_application: global-thermonuclear-war
configurables:
  CHRIS_BOGUS_TEST: 'YAY BOGUS VALUE'
  BOO_MORE_BOGUS: 'Bogons bogons everywhere'
  WOW_I_HATE_YAML: 'It is an escaping purgatory'
  LOW_GRADE_PANIC: 'Fnord.'
```
