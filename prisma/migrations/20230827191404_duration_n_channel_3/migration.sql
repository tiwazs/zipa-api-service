/*
  Warnings:

  - You are about to alter the column `cooldown` on the `ItemSkill` table. The data in that column could be lost. The data in that column will be cast from `Double` to `VarChar(191)`.
  - You are about to alter the column `cooldown` on the `TraitEffect` table. The data in that column could be lost. The data in that column will be cast from `Double` to `VarChar(191)`.

*/
-- AlterTable
ALTER TABLE `ItemSkill` MODIFY `cooldown` VARCHAR(191) NULL DEFAULT '-';

-- AlterTable
ALTER TABLE `TraitEffect` MODIFY `cooldown` VARCHAR(191) NULL DEFAULT '-';
