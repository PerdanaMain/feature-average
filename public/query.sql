CREATE TABLE IF NOT EXISTS "pf_details" (
  "id" UUID PRIMARY KEY,
  "part_id" UUID NOT NULL,
  "upper_threshold" INT NULL,
  "lower_threshold" INT NULL,
  "predict_status" VARCHAR(50) NULL,
  "time_failure" TIMESTAMP NULL,
  "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "fk_pf_details_part_id" FOREIGN KEY ("part_id") REFERENCES "pf_parts"("id")
);