-- index
-- create index using the first letter of a name
CREATE INDEX idx_name_first
ON names (name(1));
