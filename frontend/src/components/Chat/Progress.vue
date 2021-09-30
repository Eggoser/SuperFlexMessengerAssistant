<template>
    <div class="progress-bar__container w-100 h-100">
        <div class="progress-bar__main me-2">
            <div class="progress-bar__target" :style="'height: ' + (100 - height) + '%'">
            </div>
        </div>
        <div class="progress-bar__metrics">
            <div class="progress-bar__label">
                {{ name }}
            </div>
            <div class="progress-bar__counter text-color-light">
                {{ height }}%
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        height: Number,
        name: String
    }
}
</script>

<style lang="scss" scoped>
    .progress-bar {
        &__container {
            justify-content: center;
            display: flex;
        }
        
        &__main {
            height: 100%;
            width: 20px;
            display: flex;
            flex-direction: column;
            background: linear-gradient(0deg, rgba(14,167,41,1) 0%, rgba(255,74,0,1) 100%);;
        }
        &__target {
            width: 20px;
            background-color: rgba(238, 238, 238, 1);
            transition: all 0.5s ease;
        }
        
        &__metrics {
            justify-content: space-between;
            flex-direction: column;
            display: flex;
        }
        
        &__label {
            font-size: 14px;
            line-height: 16px;
            color: #d7d7d7
        }
        &__counter {
            font-size: 18px;
            line-height: 20px;
        }
    }
</style>