-- index
-- create index using the first letter of a name
CREATE INDEX idx_name_first_score
ON names (name(1), score);
