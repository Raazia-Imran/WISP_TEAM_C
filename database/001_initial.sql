-- Proposed persistence foundation. Starter API is stateless.
CREATE TABLE evidence_sources (
  id TEXT PRIMARY KEY,
  url TEXT NOT NULL,
  retrieved_at TIMESTAMPTZ NOT NULL,
  sha256 TEXT NOT NULL,
  review_status TEXT NOT NULL CHECK (review_status IN ('draft','reviewed','rejected'))
);
CREATE TABLE scenario_runs (
  id UUID PRIMARY KEY,
  parent_run_id UUID REFERENCES scenario_runs(id),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  schema_version TEXT NOT NULL,
  engine_version TEXT NOT NULL,
  input_snapshot JSONB NOT NULL,
  output_snapshot JSONB NOT NULL,
  evidence_snapshot JSONB NOT NULL
);
