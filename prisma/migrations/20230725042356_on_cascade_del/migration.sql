-- DropForeignKey
ALTER TABLE `AssignedSkillType` DROP FOREIGN KEY `AssignedSkillType_skill_id_fkey`;

-- DropForeignKey
ALTER TABLE `AssignedSkillType` DROP FOREIGN KEY `AssignedSkillType_skill_type_id_fkey`;

-- AddForeignKey
ALTER TABLE `AssignedSkillType` ADD CONSTRAINT `AssignedSkillType_skill_id_fkey` FOREIGN KEY (`skill_id`) REFERENCES `Skill`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `AssignedSkillType` ADD CONSTRAINT `AssignedSkillType_skill_type_id_fkey` FOREIGN KEY (`skill_type_id`) REFERENCES `SkillType`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
