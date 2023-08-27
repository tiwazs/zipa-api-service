-- AlterTable
ALTER TABLE `ItemSkill` MODIFY `cooldown` VARCHAR(191) NULL DEFAULT '0';

-- AlterTable
ALTER TABLE `Skill` MODIFY `cooldown` VARCHAR(191) NULL DEFAULT '0';

-- AlterTable
ALTER TABLE `TraitEffect` MODIFY `cooldown` VARCHAR(191) NULL DEFAULT '0';
