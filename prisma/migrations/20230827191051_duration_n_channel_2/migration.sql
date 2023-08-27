/*
  Warnings:

  - You are about to alter the column `duration` on the `SkillEffect` table. The data in that column could be lost. The data in that column will be cast from `Double` to `VarChar(191)`.
  - You are about to alter the column `duration` on the `SkillSummon` table. The data in that column could be lost. The data in that column will be cast from `Double` to `VarChar(191)`.
  - You are about to alter the column `duration` on the `TraitEffect` table. The data in that column could be lost. The data in that column will be cast from `Double` to `VarChar(191)`.

*/
-- AlterTable
ALTER TABLE `SkillEffect` MODIFY `duration` VARCHAR(191) NULL DEFAULT '1';

-- AlterTable
ALTER TABLE `SkillSummon` MODIFY `duration` VARCHAR(191) NULL DEFAULT '1';

-- AlterTable
ALTER TABLE `TraitEffect` MODIFY `duration` VARCHAR(191) NULL DEFAULT '1';
