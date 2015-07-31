# py-mapzen-whosonfirst-concordances

This will eventually deprecate and replace `py-woe-isthat` but not yet.

## PostGIS

```
CREATE TABLE concordances (wof_id BIGINT, other_id VARCHAR, other_src VARCHAR);
CREATE UNIQUE INDEX unq_concordance ON concordances(wof_id, other_id, other_src);
CREATE INDEX by_wof ON concordances (wof_id);
CREATE INDEX by_other ON concordances (other_src, other_id);
```