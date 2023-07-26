-- DropForeignKey
ALTER TABLE `ItemSkill` DROP FOREIGN KEY `ItemSkill_item_id_fkey`;

-- DropForeignKey
ALTER TABLE `ItemSkill` DROP FOREIGN KEY `ItemSkill_skill_id_fkey`;

-- DropForeignKey
ALTER TABLE `TraitEffect` DROP FOREIGN KEY `TraitEffect_effect_id_fkey`;

-- DropForeignKey
ALTER TABLE `TraitEffect` DROP FOREIGN KEY `TraitEffect_trait_id_fkey`;

-- DropForeignKey
ALTER TABLE `UnitItem` DROP FOREIGN KEY `UnitItem_item_id_fkey`;

-- DropForeignKey
ALTER TABLE `UnitItem` DROP FOREIGN KEY `UnitItem_unit_id_fkey`;

-- DropForeignKey
ALTER TABLE `UnitSkill` DROP FOREIGN KEY `UnitSkill_skill_id_fkey`;

-- DropForeignKey
ALTER TABLE `UnitSkill` DROP FOREIGN KEY `UnitSkill_unit_id_fkey`;

-- DropForeignKey
ALTER TABLE `UnitTrait` DROP FOREIGN KEY `UnitTrait_trait_id_fkey`;

-- DropForeignKey
ALTER TABLE `UnitTrait` DROP FOREIGN KEY `UnitTrait_unit_id_fkey`;

-- AddForeignKey
ALTER TABLE `UnitSkill` ADD CONSTRAINT `UnitSkill_unit_id_fkey` FOREIGN KEY (`unit_id`) REFERENCES `Unit`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitSkill` ADD CONSTRAINT `UnitSkill_skill_id_fkey` FOREIGN KEY (`skill_id`) REFERENCES `Skill`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitItem` ADD CONSTRAINT `UnitItem_unit_id_fkey` FOREIGN KEY (`unit_id`) REFERENCES `Unit`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitItem` ADD CONSTRAINT `UnitItem_item_id_fkey` FOREIGN KEY (`item_id`) REFERENCES `Item`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `ItemSkill` ADD CONSTRAINT `ItemSkill_item_id_fkey` FOREIGN KEY (`item_id`) REFERENCES `Item`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `ItemSkill` ADD CONSTRAINT `ItemSkill_skill_id_fkey` FOREIGN KEY (`skill_id`) REFERENCES `Skill`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitTrait` ADD CONSTRAINT `UnitTrait_unit_id_fkey` FOREIGN KEY (`unit_id`) REFERENCES `Unit`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitTrait` ADD CONSTRAINT `UnitTrait_trait_id_fkey` FOREIGN KEY (`trait_id`) REFERENCES `Trait`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `TraitEffect` ADD CONSTRAINT `TraitEffect_trait_id_fkey` FOREIGN KEY (`trait_id`) REFERENCES `Trait`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `TraitEffect` ADD CONSTRAINT `TraitEffect_effect_id_fkey` FOREIGN KEY (`effect_id`) REFERENCES `Effect`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
