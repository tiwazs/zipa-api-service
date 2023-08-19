/*
  Warnings:

  - You are about to drop the column `incoming_magical_damage` on the `Effect` table. All the data in the column will be lost.
  - You are about to drop the column `incoming_physical_damage` on the `Effect` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE `Effect` DROP COLUMN `incoming_magical_damage`,
    DROP COLUMN `incoming_physical_damage`,
    ADD COLUMN `magical_damage_infliction` VARCHAR(191) NULL,
    ADD COLUMN `physical_damage_infliction` VARCHAR(191) NULL;
