/*
  Warnings:

  - You are about to drop the column `conditions` on the `Trait` table. All the data in the column will be lost.
  - You are about to drop the column `cooldown` on the `Trait` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE `Trait` DROP COLUMN `conditions`,
    DROP COLUMN `cooldown`;

-- AlterTable
ALTER TABLE `TraitEffect` ADD COLUMN `conditions` VARCHAR(191) NULL,
    ADD COLUMN `cooldown` DOUBLE NOT NULL DEFAULT 0;
