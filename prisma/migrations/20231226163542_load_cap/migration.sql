/*
  Warnings:

  - Added the required column `base_load_capacity` to the `Unit` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE `Unit` ADD COLUMN `base_load_capacity` DOUBLE NOT NULL;

-- AlterTable
ALTER TABLE `UnitSpecialization` ADD COLUMN `load_capacity` DOUBLE NOT NULL DEFAULT 0;
