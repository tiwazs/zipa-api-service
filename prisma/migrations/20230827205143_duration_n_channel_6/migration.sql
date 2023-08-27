/*
  Warnings:

  - You are about to alter the column `essence_cost` on the `ItemSkill` table. The data in that column could be lost. The data in that column will be cast from `Double` to `VarChar(191)`.

*/
-- AlterTable
ALTER TABLE `ItemSkill` ADD COLUMN `vitality_cost` VARCHAR(191) NULL DEFAULT '0',
    MODIFY `essence_cost` VARCHAR(191) NULL DEFAULT '0';
