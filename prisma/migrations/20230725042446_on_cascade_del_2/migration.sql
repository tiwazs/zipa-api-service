-- DropForeignKey
ALTER TABLE `SkillEffect` DROP FOREIGN KEY `SkillEffect_effect_id_fkey`;

-- DropForeignKey
ALTER TABLE `SkillEffect` DROP FOREIGN KEY `SkillEffect_skill_id_fkey`;

-- AddForeignKey
ALTER TABLE `SkillEffect` ADD CONSTRAINT `SkillEffect_skill_id_fkey` FOREIGN KEY (`skill_id`) REFERENCES `Skill`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `SkillEffect` ADD CONSTRAINT `SkillEffect_effect_id_fkey` FOREIGN KEY (`effect_id`) REFERENCES `Effect`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
