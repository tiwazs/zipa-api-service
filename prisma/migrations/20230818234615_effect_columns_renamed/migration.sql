/*
  Warnings:

  - You are about to drop the column `essence_recovery` on the `Effect` table. All the data in the column will be lost.
  - You are about to drop the column `magical_damage_infliction` on the `Effect` table. All the data in the column will be lost.
  - You are about to drop the column `physical_damage_infliction` on the `Effect` table. All the data in the column will be lost.
  - You are about to drop the column `vitality_recovery` on the `Effect` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE `Effect` DROP COLUMN `essence_recovery`,
    DROP COLUMN `magical_damage_infliction`,
    DROP COLUMN `physical_damage_infliction`,
    DROP COLUMN `vitality_recovery`,
    ADD COLUMN `instant_area_of_effect` VARCHAR(191) NULL,
    ADD COLUMN `instant_conditions` VARCHAR(191) NULL,
    ADD COLUMN `instant_essence_recovery` VARCHAR(191) NULL,
    ADD COLUMN `instant_magical_damage` VARCHAR(191) NULL,
    ADD COLUMN `instant_physical_damage` VARCHAR(191) NULL,
    ADD COLUMN `instant_target` ENUM('NONE', 'SELF', 'ALLY', 'ALLY_SUMMON', 'ALLY_AROUND', 'ALLY_EXCEPT_SELF', 'ENEMY', 'ENEMY_SUMMON', 'ENEMY_AROUND', 'ANY', 'ANY_AROUND', 'ANY_EXCEPT_SELF', 'ANY_SUMMON', 'POINT', 'POINT_ENEMY', 'POINT_ALLY', 'AREA', 'AREA_ENEMY', 'AREA_ALLY') NOT NULL DEFAULT 'SELF',
    ADD COLUMN `instant_vitality_recovery` VARCHAR(191) NULL;
