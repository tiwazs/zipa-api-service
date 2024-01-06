-- AlterTable
ALTER TABLE `Race` ADD COLUMN `race_group_id` VARCHAR(191) NULL;

-- AlterTable
ALTER TABLE `UnitItem` MODIFY `equipped` BOOLEAN NULL DEFAULT false;

-- CreateTable
CREATE TABLE `RaceGroup` (
    `id` VARCHAR(191) NOT NULL,
    `name` VARCHAR(191) NOT NULL,
    `description` TEXT NOT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `Race` ADD CONSTRAINT `Race_race_group_id_fkey` FOREIGN KEY (`race_group_id`) REFERENCES `RaceGroup`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
