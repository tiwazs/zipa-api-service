-- AlterTable
ALTER TABLE `SkillEffect` MODIFY `duration` DOUBLE NOT NULL DEFAULT 1;

-- AlterTable
ALTER TABLE `SkillSummon` MODIFY `duration` DOUBLE NOT NULL DEFAULT 1;

-- AlterTable
ALTER TABLE `TraitEffect` ADD COLUMN `duration` DOUBLE NOT NULL DEFAULT 1;
