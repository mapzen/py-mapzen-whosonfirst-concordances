# py-mapzen-whosonfirst-concordances

Tools for indexing and querying Who's On First concordances in Postgres (though you could swap out the database library for any SQL database).

## Usage

### Indexing

```
    import mapzen.whosonfirst.utils
    import mapzen.whosonfirst.concordances

    cfg = ConfigParser.ConfigParser()
    cfg.read(options.config)

    dsn = mapzen.whosonfirst.concordances.cfg2dsn(cfg, 'whosonfirst')
    idx = mapzen.whosonfirst.concordances.index(dsn)

    source = os.path.abspath(options.source)
    crawl = mapzen.whosonfirst.utils.crawl(source, inflate=True)

    for record in crawl:

        props = record['properties']
        wofid = props['wof:id']

        concordances = props.get('wof:concordances', None)

        for k, v in concordances.items():
            idx.import_concordance(wofid, v, k)
```

## PostGIS

```
CREATE TABLE concordances (wof_id BIGINT, other_id VARCHAR, other_src VARCHAR);
CREATE UNIQUE INDEX unq_concordance ON concordances(wof_id, other_id, other_src);
CREATE INDEX by_wof ON concordances (wof_id);
CREATE INDEX by_other ON concordances (other_src, other_id);
```