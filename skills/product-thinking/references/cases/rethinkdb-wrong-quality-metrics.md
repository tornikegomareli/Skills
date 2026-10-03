---
id: rethinkdb-wrong-quality-metrics
product: RethinkDB
type: failure
category: dev-tool
year: 2016
principles: [launch-too-late, no-job-defined, positioning-missing-alternative]
---

**Decision.** The founders optimized the database for correctness, a simple interface, and consistency. Users wanted something else: a product that existed when they needed it, speed on their own quick tests, and a clear use case. When RethinkDB could not beat MongoDB in 2014, the team added realtime push and later started Horizon and Horizon Cloud with a small team.

**Outcome.** By the time RethinkDB was ready for production, most users asked how it was different from MongoDB. The co-founder says the product was three years behind the market. The realtime pivot put it against Meteor and Firebase, again about three years late. The cloud product never shipped before the money ran out, and the company shut down in 2016. Thousands of people used it, but almost none would pay.

**Lesson.** Users judge a product by the job they need done now and by the alternative they already know, not by the builder's idea of quality.

## Sources
- https://web.archive.org/web/20181223110526/http://www.defmacro.org:80/2017/01/18/why-rethinkdb-failed.html
- https://www.failory.com/cemetery/rethinkdb
